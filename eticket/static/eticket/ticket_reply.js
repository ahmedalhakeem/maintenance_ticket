document.addEventListener('DOMContentLoaded', ()=>{
    const select = document.querySelector('#choose-day')
    console.log(select);
    const wrap = document.querySelector('#wrap')
    wrap.style.display = 'none'

  

        // $('.allocate-btn').on('click', function(e){
        //     select.innerHTML= ''
        //     if(wrap.style.display === 'none'){
        //         wrap.style.display = 'block'
        //     }
        //     wrap.innerHTML=''
        //     const currentRow = $(this).closest('tr')
        //     const col1 = currentRow.find('td:eq(0)').text();
        //     const col2 = currentRow.find('td:eq(1)').text();
        //     const col5 = currentRow.find('td:eq(5)').text();
        //     const num = Number(col5)
            
        //     const init_option = document.createElement('option')
        //     init_option.value = 0
        //     init_option.innerHTML= "choose day"
        //     init_option.selected = true
        //     select.append(init_option)
        //     for(i=1; i<=num; i++){
        //         const option = document.createElement('option')
        //         option.innerHTML= `day ${i}`
        //         console.log(option);
        //         select.append(option)

        //     }
        //     wrap.append(select)

        // })
    $('#choose-day').on('change', function(){
        alert('changed')
    })
          
    $('#get-data').on('click', function(){
        const arr = []
        $('#tableid tbody tr').each(function(){
            const currentRow = $(this)
            const col1 = currentRow.find('td:eq(0)').text();
            const col2 = currentRow.find('td:eq(1)').text();
            const col5 = currentRow.find('td:eq(5)').text();

            const obj = {}
            obj.col1 = col1
            obj.col2 = col2
            obj.col5 = col5
            if(currentRow.find('.chk').is(":checked")){
                arr.push(obj)
                
            }
        })
        console.log(arr);
    });

});
