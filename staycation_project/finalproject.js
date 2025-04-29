let images = ["https://www.discovermoab.com/wp-content/uploads/2017/11/arches-alt-bg.jpg", "https://wildwomenexpeditions.com/wp-content/uploads/2024/01/Moab-National-Parks-Active-Adventure-hero-desk.jpg", "https://te-cdn-marketing-site.storage.googleapis.com/littleamerica/America/parnter/stay/places/usa-utah-moab-arches-national-park.jpg", "https://utahstories.com/wp-content/uploads/2022/11/MAIN_STREET_OF_MOAB._THIS_OLD_MORMON_PIONEER_TOWN_IS_THE_STARTING_POINT_FOR_TRIPS_NORTH_INTO_THE_ARCHES_NATIONAL..._-_NARA_-_545610-min.jpg"]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("pics").src = images[counter]
        counter += 1
    }else{
        counter = 0
        document.getElementById("pics").src = images[counter]
    }

}


function view(){
    if(document.getElementById("More").style.display === "block"){
            document.getElementById("More").style.display = "none"
            document.getElementById("Show").innerHTML = "Show more"
    }else{
        document.getElementById("More").style.display = "block"
        document.getElementById("Show").innerHTML = "Show less"
    }
}

