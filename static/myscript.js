// slideshow image
var slideIndex = 0;

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 5000); // Change image every 2 seconds
}

// toggle on auth
function openAuth(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";

}


function openNav() {
	document.getElementById("nav").style.marginLeft = "180px";
    document.getElementById("mySidenav").style.width = "180px";
    document.getElementById("nav").style.transition = "0.5s";
    document.getElementById("nav").style.display = "none"
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("nav").style.marginLeft= "0";
    document.getElementById("nav").style.display = "block"
}

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
  if (!e.target.matches('.db')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
  }
}

function myFunction1() {
    document.getElementById("myDropdown1").classList.toggle("show");
}

  window.onclick = function(c) {
  if (!c.target.matches('.db1')) {
    var myDropdown1 = document.getElementById("myDropdown1");
      if (myDropdown1.classList.contains('show')) {
        myDropdown1.classList.remove('show');
      }
  }
}

function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
}
window.onclick = function(f) {
  if (!f.target.matches('.db2')) {
    var myDropdown2 = document.getElementById("myDropdown2");
      if (myDropdown2.classList.contains('show')) {
        myDropdown2.classList.remove('show');
      }
  }
}


// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 23.5443967, lng: 87.3423506};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 16, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}

