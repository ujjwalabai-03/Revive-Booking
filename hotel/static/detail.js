$( document ).ready(function() {
	let x = window.location.search;
	let y = new URLSearchParams(x);
	hotel = y.get('hotel');


	$.ajax({
		url :`/api/detail/?hotel=${hotel}`,
		type : "GET",
		success: function(response){
			$('#checkout_form').attr('action',`/checkout/?hotel=${hotel}`)
			for (let hotel of response){
				let hotel_card =   `<div class="card mb-2 mycard mycard_bg">
										<div class="owl-carousel" id="image_array">
										
										</div>
										<div class="card-body" detail-card-body>
											<h2 class="card-title" style="font-weight:bolder">${hotel.name}
											<span class="badge badge-warning float-right" style="font-size:16px;border-radius:5px;">${hotel.ratings} / 5</span></h2>
											<p class="card-text"class="text-muted" style="font-size:16px;"> ${hotel.address}</p>
											<br>
											<h3 class="card-text"class="text-muted"><span style="font-size:18px;">₹</span><strong> ${hotel.price}</strong>/<span style="font-size:18px;">night</span></h3>
										</div>	
									</div>`
			
				$("#hotel_detail").append(hotel_card)
				hotel.images.forEach(function(item){
				$(".owl-carousel").append(`<div class="item" id="image-div">
												<img src="${item}" style="width:100%;height:60vh;"> 
											</div>`
											)	
				})
			}

			$('.owl-carousel').owlCarousel({
				items:2,
				margin:10,
				loop:true,
				autoplay:true,
				autoplayTimeout:2000,
				autoplayHoverPause:false
			});

		}
	});
});	


$.ajax({
		url :`/api/room/`,
		type : "GET",
		success: function(final){
			for (let room of final.rooms) {
				$('#room-body').append(`
					<tr class="clickable-row">
					<td><input type='radio' value="${room.id}" name="select_room"/></td>
					<td>${room.room_type}</td>
					<td>${room.description}</td>
					<td>${room.price}</td>
				`)
			}
			for(let option of final.options){
				$('#option-body').append(`
					<tr>
					<td><input type='radio' value="${option.id}" name="select_option"/></td>
					<td>${option.option}</td>
					<td>${option.choice}</td>
					<td>${option.price}</td>
				`)	
			}
		}
});
