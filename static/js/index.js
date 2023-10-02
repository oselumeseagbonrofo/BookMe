let school_counts = setInterval(updated_school);
let book_counts = setInterval(updated_books)
let upto = 0;
function updated_school(){
    let count = document.getElementById("school-count");
    count.innerHTML = ++upto;
    if (upto === 1){
        clearInterval(school_counts);
    }
}
function updated_books(){
    let count = document.getElementById("book-count");
    count.innerHTML = ++upto;
    if (upto === 80){
        clearInterval(book_counts);
    }
}