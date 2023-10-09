// Code logic courtsey of https://www.geeksforgeeks.org/how-to-make-animated-counter-using-javascript/
// Adds a number from 0 to a specified number at intervals
let school_counts = setInterval(updated_school);
let book_counts = setInterval(updated_books)
let counter1 = 0;
let counter2 = 0;
function updated_school(){
    let count = document.getElementById("school-count");
    count.innerHTML = ++counter1;
    if (counter1 === 2){
        clearInterval(school_counts);
    }
}
function updated_books(){
    let count = document.getElementById("book-count");
    count.innerHTML = ++counter2;
    if (counter2 === 160){
        clearInterval(book_counts);
    }
}