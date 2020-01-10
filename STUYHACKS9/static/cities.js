
function setupSearch() {
    console.log('yay')
    fetch('/api/cities')
        .then(response => response.json())
        .then(cities => {
            const searchInput = document.getElementById("myInput");
            console.log('cities: ', cities)
            const cityNames = cities.map(({name}) => name)
            autocomplete(searchInput, cityNames);
        });
}
setupSearch()
