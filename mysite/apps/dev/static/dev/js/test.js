window.onload = function(){
    if (document.querySelector('.del')){
        document.querySelector('#delete').classList.add('show');
        document.querySelector('header').classList.add('hide');
        document.querySelector('footer').classList.add('hide');
        let container = document.querySelectorAll('.container');
        for(let i of container){
            i.classList.add('hide');
        } 
    } else if (document.querySelector('.error')){
        add_class();
        document.querySelector('.message').style.background = 'red';
        change_input();
    } else if (document.querySelector('#id_date').value){
        if (document.querySelector('.errorlist')){
            document.querySelector('.message').style.background = 'red';
        }
        add_class();
        document.querySelector('#change').classList.add('show');
        document.querySelector('header').classList.add('hide');
        let container = document.querySelectorAll('.container');
        for(let i of container){
            i.classList.add('hide');
        }
        change_input();

    } else if (location.href == "http://10.145.32.61/dev/create") {
        add_class();
        document.querySelector('.message').style.padding = '0';
        if (document.querySelector('.accept')){
            let message = document.querySelector('.message');
            message.style.background = '#28a745';
            message.style.padding = '16';
        }
        for (let i of form_array()){
            let input = document.querySelector(i);
            input.addEventListener('input', function(){
                let value = this.value
                let value_to_send = document.querySelector(`${i}_list option[value="${value}"]`).dataset.value;
                let hidden_input = input.previousElementSibling;
                hidden_input.name = this.name;
                hidden_input.id = this.id;
                this.name = '';
                hidden_input.value = value_to_send;
            })
        }
        
    }
}




// //window.onload = remove_attr_required();


// // if (document.querySelector('#id_date')){
// //     document.querySelector('#change').classList.add('show');
    
//     let input = document.querySelectorAll('input');
//     document.querySelector('textarea').classList.add('search-input');
//     //document.querySelector('header').classList.add('hide');
//     // let container = document.querySelectorAll('.container');
//     let label = document.querySelectorAll('label');
//     for (let i of input){
//         if (i.type != 'hidden' && i.type != 'search' && i.type != 'submit'){
//             i.classList.add('search-input')
//         }
//     }
//     for (let i of label){
//         i.classList.add('form-label');
//     }

//     // for(let i of container){
//     //     i.classList.add('hide');
//     // }
// }



// // function remove_attr_required(){
// //     const INV_NUM_FIELD = document.querySelector('#id_inv_number');
// //     const NOTE_FIELD = document.querySelector('#id_note');
// //     const SELLER_FIELD = document.querySelector('#id_seller');
// //     const DATE_OF_SALE_FIELD = document.querySelector('#id_date_of_sale');
// //     let tag_for_remove = [INV_NUM_FIELD, NOTE_FIELD, SELLER_FIELD, DATE_OF_SALE_FIELD];
// //     for (let i of tag_for_remove){
// //         i.removeAttribute('required');
// //     }
// // }












