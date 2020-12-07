$(document).ready(function() {
	/*
  Add smooth scrolling to all links, 
  while keeping cross-browser compatibility.
  https://www.w3schools.com/howto/howto_css_smooth_scroll.asp
  */
	$('a').on('click', function(event) {
		if (this.hash !== '') {
			event.preventDefault();

			let hash = this.hash;

			$('html, body').animate(
				{
					scrollTop: $(hash).offset().top
				},
				800,
				function() {
					window.location.hash = hash;
				}
			);
		}
	});

	/*
  When the user scrolls down, hide the navbar and
  when the user scrolls up, show the navbar.
  https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp
  */
	let prevScrollpos = window.pageYOffset;
	window.onscroll = function() {
		let currentScrollPos = window.pageYOffset;
		if (prevScrollpos > currentScrollPos) {
			document.getElementById('custom-navbar').style.top = '0';
		} else {
			document.getElementById('custom-navbar').style.top = '-63px';
		}
		prevScrollpos = currentScrollPos;
	};

	// show alerts with animation & hide them after showing.
	$('.alert').first().hide().slideDown(500).delay(4000).slideUp(500, function() {
		$(this).remove();
	});

	//DataTable settings
	let table = $('#dataTable').DataTable({
		lengthChange: false,
		dom: 'lrtip',
		info: false,
		paging: false,
		bSort: false,
		responsive: true
	});
});
