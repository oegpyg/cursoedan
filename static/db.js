const host = "http://localhost:8000/";

export const getFaseGrupoPaises = () => {
    let result = new Promise((resolve, reject) => {
        var requestOptions = {
            method: "GET",
            redirect: "follow",
        };
        fetch(`${host}api/fgp`, requestOptions)
            .then((response) => response.text())
            .then((result) => {
                resolve(JSON.parse(result));
            })
            .catch((error) => console.log("error", error));
    });
    return result;
}




