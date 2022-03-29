document.addEventListener('DOMContentLoaded', ()=>{
    console.log('working');
})
function view_edit_ticket(id){
    const submit_btn = document.querySelector('#submit-edit-ticket')
    const ticket_type = document.querySelector('#ticket-type')
    const ticket_title = document.querySelector('#ticket-title')
    const ticket_st_date = document.querySelector('#ticket-start-date')
    const tour_days = document.querySelector('#tour-days')
    const ticket_end_date = document.querySelector('#ticket-end-date')
    const tour_team = document.querySelector('#tour-team')
    console.log(id);
    fetch(`./ticket_info/${id}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error);
        })
    })
    .then(data=>{
        console.log(data);
        ticket_title.value= `${data.tour_name}`
        ticket_type.value = `${data.tour_type}`
        ticket_st_date.value = `${data.tour_date}`
        tour_days.value = `${data.tour_duration}`
        ticket_end_date.value = `${data.expected_end_tour}`
        tour_team.value = `${data.notes}`
    })
      submit_btn.addEventListener('click', (e)=>{
          fetch(`saved_edited_ticket/${id}?title=${ticket_title.value}&tic_type=${ticket_type.value}&st_date=${ticket_st_date.value}
          &days=${tour_days.value}&end_date=${ticket_end_date.value}&team=${tour_team.value}`)
          .then(res=>{
              if(res.ok) return res.json()
              return res.json()
              then(error=>{
                  console.log(error);
              })
          })
          .then(data=>{
              console.log(data);
          })
        //   e.preventDefault()
      }) 
}
