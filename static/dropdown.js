// To Do:
// Have the dropdown code be in dropdown.js, not in the HTML itself, for better readability later.
// Currently this is "placeholder", meaning it's not actually active. The code in index.html is the active one. 

let inp = document.getElementById("industry")
let arr = [
"Accounting",
"Airbnb",
"Art",
"Book Store",
"Breeding",
"Car Rentals",
"Car Repairs",
"Casino",
"Chiropractor",
"Church",
"Civil Engineering",
"Computer Repairs",
"Concert",
"Dentistry",
"Dining",
"Education",
"Electrical Engineering",
"Equipment Rental",
"Farm Stand",
"Fashion",
"Fast Food",
"Financial Advising",
"Fishing",
"Garden Center",
"Healthcare",
"Historical Site",
"Investor",
"Landscaping",
"Masonry",
"Manufacturing",
"Marketing Agency",
"Mechanical Engineering",
"News",
"Office Support Services",
"Painting",
"Phone Repairs",
"Plumbing",
"Printing",
"Radio",
"Real Estate",
"Resort",
"Roofing",
"Sanitation",
"Self Storage",
"Sporting Event",
"Steak House",
"Towing",
"Warehousing",
"Pastry Shop",
"Bakery",
"Pizzeria",
"Fine Dining",
"Cafe",
"Coffee Shop",
"Brewery",
"Ice Cream Shop",
"Health food",
"Mexican Cuisine",
"Chinese Cuisine",
"Japanese Cuisine"
]

function autocomplete(inp, arr) {
    
    var currentFocus;
    
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        
        this.parentNode.appendChild(a);
        
        for (i = 0; i < arr.length; i++) {
            
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            
            b = document.createElement("DIV");
            
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            
                b.addEventListener("click", function(e) {
                
                inp.value = this.getElementsByTagName("input")[0].value;
                
                closeAllLists();
            });
            a.appendChild(b);
            }
        }
    });
    
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            
            currentFocus++;
            
            addActive(x);
        } else if (e.keyCode == 38) { 
            
            currentFocus--;
            
            addActive(x);
        } else if (e.keyCode == 13) {
            
            e.preventDefault();
            if (currentFocus > -1) {
            
            if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {
        
        if (!x) return false;
        
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
        
        for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
        }
    }
    }
    
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}
autocomplete(inp,arr)