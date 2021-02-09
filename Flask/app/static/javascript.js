
let facts = [
    'A group of penguins in the water is called a raft but on land they’re called a waddle!',
    'The black and white “tuxedo” look donned by most penguin species is a clever camouflage called countershading. When swimming, the black on their backs helps them blend in with the darkness of the ocean from predators viewing from above. Their white bellies help them blend in with the bright surface of the ocean when viewed by predators and prey from below.',
    'Penguins may huddle together for several reasons. This behavior helps these birds protect themselves from predators. In frigid habitats, huddling helps penguins retain warmth.',
    'Penguins evolved to fly underwater. Most birds have hollow, air-filled bones to help them stay light for flight. Penguins adapted with solid bones instead. This helps them swim because solid bones reduce buoyancy—the tendency to float.',
    'A penguin’s thick feathers aren’t the only way this bird stays warm. A gland near the base of its tail provides waterproof oil. Penguins spend several hours each day covering their feathers with this oil and give extra attention to the task before swimming.',
    'Penguins live in many locations and habitats. You can find them in Antarctica and Antarctic islands, the Galapagos Islands off the coast of Ecuador, South Africa, New Zealand, Australia, Peru and Chile.',
    'Contrary to many popular holiday cartoons, you’ll never see penguins and polar bears together in the wild. That’s because penguins live south of the equator while polar bears north of the equator in Arctic!',
    'Penguin feet are adapted to walk long distances. Some species of penguins can march up to about 60 miles across sea ice to get to their breeding grounds. Penguin feet are also adapted to help the birds steer while swimming. They use their feet like rudders, angling them to help control direction.',
    'Many male penguins gift female penguins with rocks in order to woo them. The ladies use these rocks to build a nest.',
    'According to some animal experts, the penguin is one of the most streamlined animals in the world. A penguin’s body is tapered at both ends and it has a large head, short neck and elongated body. This streamlined design helps penguins swim fast. ',
    'Penguins can drink sea water.',
    'The Emperor Penguin is the tallest of all penguin species, reaching as tall as 120 cm (47 in) in height',
    'Emperor Penguins can stay underwater for around 20 minutes at a time.',
    'Chinstrap Penguins get their name from the thin black band under their head. At times it looks like they’re wearing a black helmet, which might be useful as they’re considered the most aggressive type of penguin.',
    'Penguins in Antarctica have no land based predators',
    'Yellow eyed penguins (or Hoiho) are endangered penguins native to New Zealand. Their population is believed to be around 4000.'
]




function newFact() {
    let randomNum = Math.floor(Math.random() * (facts.length));

    document.getElementById("factDisplay").innerHTML = facts[randomNum];
}




window.onload = choosePic;

let myPix = ["penguin_ad.jpg","penguin_ad2.jpg", "penguin_ad3.jpg", "penguin_ad4.jpg", "penguin_ad5.jpg"];

function choosePic() {
    let randomNum2 = Math.floor(Math.random() * myPix.length);
    document.canvas.src = "/static/ads/"+myPix[randomNum2];
}