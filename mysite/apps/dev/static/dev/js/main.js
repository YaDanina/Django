function change_input(){
    for (let i of form_array()){
        let input = document.querySelector(i);
        let hidden_input = input.previousElementSibling;
        let value_to_change = document.querySelector(`${i}_list option[data-value="${input.value}"]`).value;
        hidden_input.name = input.name;
        input.name = '';
        hidden_input.value = input.value;
        input.value = value_to_change;
    };
    for (let i of form_array()){
        let input = document.querySelector(i);
        input.addEventListener('input', function(){
            let value = this.value
            let value_to_send = document.querySelector(`${i}_list option[value="${value}"]`).dataset.value;
            let hidden_input = input.previousElementSibling;
            hidden_input.id = this.id;
            hidden_input.value = value_to_send;
        })
    }
};

// function add_event_for_input(){
//     let value = this.value
//     let value_to_send = document.querySelector(`${i}_list option[value="${value}"]`).dataset.value;
//     let hidden_input = input.previousElementSibling;
//     hidden_input.name = this.name;
//     hidden_input.id = this.id;
//     this.name = '';
//     hidden_input.value = value_to_send;

// };


function form_array(){
    let ArrId = new Array;
    let input  = document.querySelectorAll('input[type="hidden"]');
    for (let i of input){
        if (i.id){
            let input = i.nextElementSibling;
            ArrId.push('#' + input.id);
        };
    };
return ArrId;
};

function add_class(){
    let input = document.querySelectorAll('input');
    let label = document.querySelectorAll('label');
    document.querySelector('textarea').classList.add('search-input');
    for (let i of input){
        if (i.type != 'hidden' && i.type != 'search' && i.type != 'submit'){
            i.classList.add('search-input')
        }
    }
    for (let i of label){
        i.classList.add('form-label');
    }

};

function hide_show(element_for_show){
    document.querySelector(`${element_for_show}`).classList.add('show');
    document.querySelector('header').classList.add('hide');
    document.querySelector('footer').classList.add('hide');
    let container = document.querySelectorAll('.container');
    for(let i of container){
        i.classList.add('hide');
    }
}

function error (){
    document.querySelector('.message').style.background = 'red';
}




