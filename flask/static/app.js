function execute() {
  const dbms = document.getElementById("dbms").value;
  const query = document.getElementById("sqlQuery").value;

  fetch(`/query/${dbms}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ query: query })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
      document.getElementById("result").textContent = "❌ Error: " + error;
    });
}

// Suggest default query on DBMS selection
document.getElementById("dbms").addEventListener("change", function () {
  const dbms = this.value.toUpperCase();
  let defaultQuery = "";

  switch (dbms) {
    case "MYSQL":
    case "MSSQL":
      defaultQuery = "SELECT @@version;";
      break;
    case "POSTGRESQL":
      defaultQuery = "SELECT version();";
      break;
    case "ORACLE":
      defaultQuery = "SELECT banner FROM v$version;";
      break;
    case "SQLITE":
      defaultQuery = "SELECT sqlite_version();";
      break;
  }

  document.getElementById("sqlQuery").value = defaultQuery;
});
