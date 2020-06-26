if (document.querySelector('.del')){
    let element_for_show = '#delete'
    hide_show(element_for_show);
} 

if (document.querySelector('.upd')){
    let element_for_show = '#change';
    add_class();
    hide_show(element_for_show);
    change_input();
}

if (document.querySelector('.error')){
    error();
}

