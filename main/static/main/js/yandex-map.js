var myMap;

ymaps.ready(init);

function init () {
    myMap = new ymaps.Map('map', {
        center: [54.764838, 83.093364],
        zoom: 16
    }, {
        searchControlProvider: 'yandex#search'
    });

        myGeoObject = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: [54.764800, 83.093600]
            },
            properties: {
                iconCaption: 'Мы здесь!',
                hintContent: 'Да-да, вот в этом самом здании!',
            }
        }, {
            preset: 'islands#greenDotIconWithCaption',
            draggable: false,
            iconColor: '#04af86'
        });

    myMap.geoObjects
        .add(myGeoObject)
}