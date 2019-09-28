
class TestMarkArea {
  //Its funciton create lines in bordeer of divs//
   divmarker(){
    let elements = document.getElementsByTagName("div");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.border = "thick solid #0000FF";
      }
  }
}
