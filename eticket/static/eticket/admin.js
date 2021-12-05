document.addEventListener('DOMContentLoaded', ()=>{
    console.log('loaded');
})

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
        alert(`اضافة المركبة(${carinput})الى قائمة المركبات`);
    })
    location.reload();
})
// show drivers

function showInputdrivers(){
    const showinputdriver = document.querySelector('#show-Inputdrivers')
    if(showinputdriver.style.display==='none'){
        showinputdriver.style.display='block'
    }else{
        showinputdriver.style.display='none'
    }
}
const insert_driver = document.querySelector('#insert-driver');
insert_driver.addEventListener('click', ()=>{
    const driver_input = document.querySelector('#driverinput').value;
    fetch(`./add_driver?driver=${driver_input}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error);
        })
    })
    .then(data=>{
        console.log(data);
        alert(`تم اضافة ${driver_input} الى قائمة سائقي المركبات`)
    })
})