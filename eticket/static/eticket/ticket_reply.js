document.addEventListener('DOMContentLoaded', ()=>{
    // const allocate_btn = document.querySelector('#allocate-btn')
    // console.log(allocate_btn.parentElement.children);
    const wrap = document.querySelector('#wrap')

    const allocation = document.querySelector('.allocate-btn');
    const table = document.querySelector('#tableid')
    const rows = document.getElementsByTagName('tr')
    for(i=1; i<=rows.length; i++){
        let row = table.rows[i]
        // console.log();
        row.onclick = function(){
            let cell = this.getElementsByTagName('td')[5];
            console.log(cell);
        }
    }
    console.log(table);
})
    // allocation.addEventListener('click', (e)=>{
    //     e.preventDefault()
    //     const parent = e.target.parentElement.parentElement
    //     const num_days = parent.children[5].innerHTML
    //     console.log(typeof(num_days));
    //     console.log(parent.children[5]);
    //     const days =  document.querySelector('#tour-duration').innerHTML
    //     const integer = Number(days);
    //     const select = document.createElement('select')
    //     for(let i=1 ; i<= integer; i++){
    //         const option = document.createElement('option')
    //         option.innerHTML = `day ${i}`
    //         select.append(option)
    //         wrap.append(select);
    //     }
    //     console.log(select); 
           
    // })
    

