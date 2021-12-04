document.addEventListener('DOMContentLoaded', ()=>{
    const department = document.querySelector('#department')
    const section = document.querySelector('#section')

    department.addEventListener('change', (e)=>{
        section.innerHTML='';
        console.log(e.target.value);
        if(e.target.value==='1'){
            fetch("./get_sections")
            .then((res)=>{
                if(res.ok) return res.json()
                return res.json()
                .then(error=>{
                    console.log(error);
                })
            })
            .then((data)=>{
                console.log(data);
                data.forEach(value=>{
                    section.innerHTML += `<option>${value.section_name}</option>`
                })
            })
        }else{
            fetch("./get_all_non_dept_sections")
            .then(res=>{
                if(res.ok) return res.json()
                return res.json()
                .then(error=>{
                    console.log(error)
                })
            })
            .then((data)=>{
                console.log(data);
                data.forEach(value=>{
                    section.innerHTML += `<option>${value.section_name}</option>`
                })

            })    
        }
    })
})