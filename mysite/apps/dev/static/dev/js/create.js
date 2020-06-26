add_class();
document.querySelector('.message').style.padding = '0';
if (document.querySelector('.accept')){
    let message = document.querySelector('.message');
    message.style.background = '#28a745';
    message.style.padding = '16px';
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


if (document.querySelector('.error')){
    error();
    change_input();
}



