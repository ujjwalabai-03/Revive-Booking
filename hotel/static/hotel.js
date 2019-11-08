$( document ).ready(function() {
    let x = window.location.search;
	let y = new URLSearchParams(x);
	city = y.get('city');


	$.ajax({
	url :`/api/hotel/?city=${city}`,
	type : "GET",
	success: function(response){
		for (let list of response){
			let hotel_list_card = `<a href="http://127.0.0.1:8000/hotel_detail?city=${city}&hotel=${list.id}">
									<div class="card mb-2 mycard mycard_bg" style="max-width: 100%; border-radius: 5px;">
										<div class="row no-gutters">
											<div class="col-md-4" id="image_array">
												<img src="${list.images[0]}" width="200" height="150">
											</div>
											<div class="col-md-8">
												<div class="card-body hotel-card-body">
													<h2 class="card-title" style="font-weight:bolder">${list.name} <span class="badge badge-warning float-right" style="font-size:16px;border-radius:5px;"> ${list.ratings} / 5</span></h2>
													<br>
													<h1 class="card-text"class="text-muted"><span style="font-size:24px;">₹</span><strong> ${list.price}</strong>/<span style="font-size:24px;">night</span></h1>
												</div>
											</div>
										</div>
									</div>
								</a>`
			$("#hotel_list").append(hotel_list_card)
		}
	}
});
});




