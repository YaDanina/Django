let copy_btn = document.querySelectorAll('.copy_btn')
for (let i of copy_btn){
    i.addEventListener('click', function(){
        let input = i.previousElementSibling
        input.select()
        document.execCommand('copy')
    })

}