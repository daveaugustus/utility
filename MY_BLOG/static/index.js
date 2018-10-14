// 1. get all Signup instructions and disable remove when document loads
let instructions = document.getElementsByTagName('small');
document.addEventListener('DOMContentLoaded', removeInstructions);

function removeInstructions(){
    for(let i=0; i<instructions.length; i++){
        instructions[i].style.display = 'none'
    }
    
}