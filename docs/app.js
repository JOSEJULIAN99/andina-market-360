fetch("data/resumen.json")
  .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
  .then((datos) => {
    document.getElementById("operaciones").textContent = datos.operaciones;
    document.getElementById("total").textContent = "S/ " + datos.total;
    document.getElementById("fuente").textContent = datos.fuente;
    const total = Number(datos.total);
    document.getElementById("sedes").innerHTML = Object.entries(datos.sedes)
      .map(([sede, monto]) => {
        const pct = ((Number(monto) / total) * 100).toFixed(1);
        return `<tr><td>${sede}</td><td>${monto}</td><td><div class="participacion"><div class="barra" style="width:${pct}%"></div><span>${pct} %</span></div></td></tr>`;
      }).join("");
  })
  .catch(() => {
    document.getElementById("sedes").innerHTML =
      '<tr><td colspan="3">No se encontró data/resumen.json. Ejecute python src/resumen.py --json docs/data/resumen.json</td></tr>';
  });
