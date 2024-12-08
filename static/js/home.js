window.onload = () => {
    validation();
}
document.addEventListener('DOMContentLoaded', () => {
});

function validation() {
    //Función que sirve para evitar mandar resultados vacios y que no se rompa el programa
    const get_procentaje = document.getElementById("test_size");
    // console.log(get_procentaje)
    if (get_procentaje) {
        const train_model = document.getElementById("train_model");
        if (get_procentaje.value == "1.0") {
            train_model.disabled = true;
        }
        get_procentaje.addEventListener("click", () => {
            // console.log(get_procentaje.options[get_procentaje.selectedIndex].textContent);
            document.getElementById("test_size_text").value = get_procentaje.options[get_procentaje.selectedIndex].textContent;

            if (get_procentaje.value == "1.0") {
                train_model.disabled = true;
            } else {
                train_model.disabled = false;
            }
        });
    }
}
const iris_data = document.querySelector(".iris_data");
const train_info = document.getElementById("train_info");
if (train_info) {
    if (train_info.textContent == "") {
        iris_data.classList.add("off")
        iris_data.classList.remove("on")
    } else {
        iris_data.classList.add("on")
        iris_data.classList.remove("off")
    }

}
