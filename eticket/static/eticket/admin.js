document.addEventListener('DOMContentLoaded', ()=>{
    console.log('loaded');
})
function showCars(){
    const availablecars = document.querySelector('#add-car')
    if(availablecars.style.display === 'none'){
        availablecars.style.display='block';
    }else{
        availablecars.style.display='none';
    }
}
function showInputcars(){
    const show_input_cars = document.querySelector('#show-Inputcars');
    if(show_input_cars.style.display==='none'){
        show_input_cars.style.display='block'
    }else{
        show_input_cars.style.display='none'
    }
}
const add_new_car = document.querySelector('#insert-car')
add_new_car.addEventListener('click', ()=>{
    const carinput = document.querySelector('#carinput').value;
    fetch(`./add_car?car=${carinput}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error);
        })
    })
    .then((data)=>{
        alert(data.message);
    })
    location.reload();
})
