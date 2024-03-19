function updateTask(el){
    task_id = el.value
    fetch('/ready/' + task_id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'ready': el.checked})
    })
}

function createTask(){
    console.log('Create')
    let todo = document.getElementById('todo').value
    let deadline = document.getElementById('deadline').value

    fetch('/task', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'todo': todo || 'Пустое', 'deadline': deadline || '12.12.24', 'ready': false})
    })

}

window.onload = ( () => {
    document.getElementById('deadline').valueAsDate = new Date()
})