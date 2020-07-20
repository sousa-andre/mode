let formset = document.querySelector('#form_set');
let addButton = document.querySelector('#add-new');
let removeButton = document.querySelector('#remove-last');
let totalFormsInput = document.querySelector('#id_form-TOTAL_FORMS');
let emptyForm = document.querySelector('#empty-form');

addButton.addEventListener('click', ()=>{
    totalFormsInput.value++;

    let element = document.createElement('div');

    element.setAttribute('class', 'input-group');
    formset.appendChild(element).innerHTML = emptyForm.innerHTML.replace(/__prefix__/, totalFormsInput.value);
});
removeButton.addEventListener('click', ()=>{
   totalFormsInput.value--;
   let inputGroups = formset.getElementsByClassName('input-group');
   if (inputGroups.length < 2) return;
   formset.removeChild(inputGroups[inputGroups.length-1]);
});
