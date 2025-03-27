#!/bin/bash

PROJECT_NAME="final"
COMPOSE_FILE="docker-compose.yml"
WEB_SERVICE_NAME="web"  # Make sure this matches the name in your docker-compose.yml

function start_containers() {
    echo "🚀 Starting containers..."
    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE up -d; then
        echo "❌ Failed to start containers."
        usage
    fi
}

function stop_containers() {
    echo "🛑 Stopping containers..."
    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE down; then
        echo "❌ Failed to stop containers."
        usage
    fi
}

function clean_install() {
    echo "🧼 Cleaning up old containers, volumes, and networks..."
    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE down -v --remove-orphans; then
        echo "❌ Failed to clean up old containers."
        usage
    fi

    echo "🔨 Rebuilding and starting fresh..."
    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE build --no-cache; then
        echo "❌ Build failed."
        usage
    fi

    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE up -d; then
        echo "❌ Failed to start containers after rebuild."
        usage
    fi
}

function rebuild_web() {
    echo "🧹 Stopping and removing existing web container..."
    docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE stop $WEB_SERVICE_NAME || true
    docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE rm -f $WEB_SERVICE_NAME || true

    echo "🧼 Removing dangling images (if any)..."
    docker image prune -f || true

    echo "🔁 Rebuilding the web service..."
    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE build --no-cache $WEB_SERVICE_NAME; then
        echo "❌ Failed to build web container."
        usage
    fi

    echo "🚀 Starting the web container..."
    if ! docker-compose -p $PROJECT_NAME -f $COMPOSE_FILE up -d $WEB_SERVICE_NAME; then
        echo "❌ Failed to start web container."
        usage
    fi

    echo "✅ Web container successfully rebuilt and started."
}

function usage() {
    echo ""
    echo "Usage: ./SQL_Ground-Manager.sh [start|stop|clean|rebuild]"
    echo ""
    echo "   start    → Start all containers"
    echo "   stop     → Stop all containers"
    echo "   clean    → Remove everything and do a clean install"
    echo "   rebuild  → Rebuild only the web container"
    echo ""
    exit 1
}

# Handle script interruption (Ctrl+C)
trap 'echo -e "\n⚠️  Script interrupted. Returning to menu."; usage' INT

case "$1" in
    start)
        start_containers
        ;;
    stop)
        stop_containers
        ;;
    clean)
        clean_install
        ;;
    rebuild)
        rebuild_web
        ;;
    *)
        usage
        ;;
esac
