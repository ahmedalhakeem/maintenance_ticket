document.addEventListener('DOMContentLoaded', ()=>{
    const result = document.querySelector('#result')
    result.style.display = 'none';
})
function show_retrived(){
    result.style.display='block';
    const type = document.querySelector('#type').value;
    const start = document.querySelector('#start-date').value;
    const end = document.querySelector('#end-date').value;
    const content = document.querySelector('#content')
    content.innerHTML=''
    fetch(`./show_specified?type=${type}&start=${start}&end=${end}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error)
        })
    })
    .then(data=>{
        console.log(data);
        data.data.forEach(value=>{
            console.log(value.employee);
            const tr = document.createElement('tr')
            tr.innerHTML=''
            tr.innerHTML = `<td> ${value.id}</td> <td>${value.user}</td> <td> ${value.tour_name}</td><td>${value.tour_type}</td><td>${value.tour_date}</td><td>${value.tour_duration}</td>
                            <td>${value.expected_end_tour}</td><td>${value.notes}</td>`
            content.append(tr)
        })
        
        
    })
    // location.reload();
}