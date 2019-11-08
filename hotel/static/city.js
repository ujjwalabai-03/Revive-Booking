//fetching city from backend
$.ajax({
	url :"/api/city/",
	type : "GET",
	success: function(response){
		for (let city of response){
			let city_card = `<a href="http://127.0.0.1:8000/hotel_list?city=${city.name}">
								<div class="card mb-2 mycard mycard_bg" style="max-width: 100%; border-radius: 5px;">
									<div class="row no-gutters">
										<div class="col-md-4">
											<img src="${city.image}" width="200" height="150">
										</div>
										<div class="col-md-8">
											<div class="card-body city-card-body">
												<h2 class="card-title" style="font-weight:bolder">${city.name}</h2>
												<p class="card-text"class="text-muted">
												<span class="badge badge-primary disabled pill">Hotels</span>
												<span class="badge badge-primary disabled pill">Resorts</span>
												<span class="badge badge-primary disabled pill">Villas</span>
												<span class="badge badge-primary disabled pill">Budget Hotels</span>
												</p>
											</div>
										</div>
									</div>
								</div>
							</a>`
			$("#suggestions").append(city_card)
		}
	}
});

// $('#dropdownMenuButton').on("click", function(e){
// 	console.log(e);
// })

// $("body").on('change', '#call', function() {
//     //get the selected value
//     var selectedValue = $(this).val();

//     //make the ajax call
//     $.ajax({
//         url: 'ajax.php',
//         type: 'POST',
//         data: {option : selectedValue},
//         success: function() {
//             console.log("Data sent!");
//             alert("this");
//         }
//     });
// });

