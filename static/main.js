import {
    getFaseGrupoPaises,
} from "./db.js"

getFaseGrupoPaises().then((res) => {
    let htmlCards = '';
    let predicciones = {};

    res.forEach((card) => {
        htmlCards += `<div class="card">
            <h4>Grupo ${card.grupo}</h4>
            <hr>
            <div class="row">
              ${card.paises.map((c) =>
            `<div id="btn-${card.grupo}-${c.codigo}-${c.icono}" class="btn">
                    <img class="paisImagen" src="${c.icono}"/>${c.codigo}
                </div>`
        )}
            </div>
            <div>
                <div id="seleccionado-0-${card.grupo}">1.__________</div>
                <div id="seleccionado-1-${card.grupo}">2.__________</div>
                <div id="seleccionado-2-${card.grupo}">3.__________</div>
                <div id="seleccionado-3-${card.grupo}">4.__________</div>
            </div>
        </div > `;
    });
    document.querySelector("#container").innerHTML = htmlCards;

    let botones = document.querySelectorAll(".btn");
    botones.forEach((btn) => {
        btn.onclick = (event) => {
            let group = btn.id.split("-")[1];
            let pais = btn.id.split("-")[2];
            let icono = btn.id.split("-")[3];
            if (!predicciones[group]) predicciones[group] = [];
            if (predicciones[group].length < 4 && predicciones[group].indexOf(pais) === -1) {
                document.querySelector(`#seleccionado-${predicciones[group].length}-${group}`)
                    .innerHTML = `${predicciones[group].length + 1} - <img class="paisImagen" src="${icono}"/>${pais}`;
                predicciones[group].push(pais);
            }
        }
    })
});