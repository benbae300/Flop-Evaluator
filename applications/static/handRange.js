import {Flop, Models} from './createModels.js';
var heroRange = undefined; 
var clickedRange = false;

const navBarHeight = 70;
const models = new Models();
const hands = new Models();
const whichFlop = ['0', '0', '0'];
const whichHand = ['0', '0']; 
const cardRank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'];
const split = window.location.href.split('?');
const range1 = split[2];
const range2 = split[3];
const URL = split[0]; 

$(document).ready(function() {
    initLayout();
    initCards();
});

function initLayout() {
    setContainerHeight(window.innerHeight - navBarHeight);
    window.onresize = reportWindowSize;
    $('#b-btn')[0].style.visibility = 'hidden';

    document.getElementById('drop0').textContent += range1;
    document.getElementById('drop1').textContent += range2;
    document.getElementById("which_flop").textContent += split[1] + ': ' + split[2] + ' vs ' + split[3];

    $('#myButton').click(function() { calculateEquity(); })
    $('#range').click(function() { window.location.replace('allRangesHands'); })
}

function initCards() 
{
    initTop();     
    setDeck('S');
    setDeck('C');
    setDeck('D');
    setDeck('H');
    monitorUserClick();
}

function reportWindowSize(){ setContainerHeight(window.innerHeight - navBarHeight); }

function setContainerHeight(height) {  $('#c-container').height(height + 'px'); }

function calculateEquity(){
    var equityDiv = document.getElementById('findEquity');
        equityDiv.innerHTML = ''; 
        equityDiv.textContent += 'Calculating...';
        var sendData = { 
            action: split[1],
            r1: split[2],
            r2: split[3],
            h1: whichHand[0], 
            h2: whichHand[1],
            pos: heroRange,
            f1: whichFlop[0],
            f2: whichFlop[1],
            f3: whichFlop[2]
        }; 
        $.ajax({
            url: URL,
            type: "POST",
            data: JSON.stringify(sendData),
            contentType: 'application/json',
            dataType: 'json',
            success: function (e) {
                var equityDiv = document.getElementById('findEquity');
                equityDiv.innerHTML = ''; 
                equityDiv.textContent += e['equity'];
            },
            error: function(error) {
                console.log(error);
            }
        });
}

function initTop()
{
    initFlop();
    initHand();
}

function initFlop(){
    for(var i=0;i<3;++i) {
        var flop = new Flop();
        $('#flop-' + i).append(`<img id="back-image" src="/static/assets/Red_back.jpg"/>`);
        models.flops.push(flop);
    }
}

function initHand(){
    for(var i=0;i<2;++i) {
        var hand = new Flop();
        $('#hand-' + i).append(`<img id="back-image" src="/static/assets/Red_back.jpg"/>`);
        hands.flops.push(hand);
    }
}

function setDeck(currentSuit) 
{
    for(var i = 0; i < 13; i++){
        var currentCardRank = cardRank[i];
        $(`#${currentSuit}`).append(`<div class=deck-card id=${currentSuit}-${currentCardRank}></div>`);
        $(`#${currentSuit}-${currentCardRank}`).append(`<img id="${currentCardRank}${currentSuit}" src="/static/assets/${currentCardRank}${currentSuit}.png" />`);
    }
}

function monitorUserClick()
{
    $(document).on("click", ".drop-bu", function(event) 
    {
        let buID = $(this).attr('id');
        if (buID == 'drop0') heroRange = range1;  
        else heroRange = range2;  
        let buttonText = document.getElementById('pos-but');
        buttonText.innerHTML = ''; 
        buttonText.textContent += "Current Position:  " + heroRange; 
        clickedRange = true; 
        checkButtonVisibility();
    })
    $(document).on("click", ".b-flop", function(event) {monitorTop('flop', models, event.target.id, $(this).attr('id'));})
    $(document).on("click", ".b-hand", function(event) {monitorTop('hand', hands, event.target.id, $(this).attr('id'));})

    $(document).on("click", ".deck-card", function(event) 
    {
        const id = event.target.id;
        if (id.length > 2) return; 
        setClickFlop(id);
    })
}

function monitorTop(divName, divFlop, id, picID){
    if (id.length > 3) return; 
    onTopClicked(picID.split('-')[1], id, divName, divFlop);
    $('#b-btn')[0].style.visibility = 'hidden';
}


function onTopClicked(num, id, divName, divFlop){
    var equityDiv = document.getElementById('findEquity');
    equityDiv.innerHTML = ''; 
    equityDiv.textContent += 'N/A';
    let rank = id.charAt(0);
    let suit = id.charAt(1);
    appendCard(`#${divName}-`+ num, 'back-image', 'Red_back.jpg'); 
    appendCard(`#${suit}-${rank}`, `${id}`, `${id}`+'.png');
    divFlop.flops[parseInt(num)].status = true;

}

function setClickFlop(id) 
{
        let isFlop = onClicked(id, models, 'flop', whichFlop);
        if(isFlop == false) onClicked(id, hands, 'hand', whichHand); 
        checkButtonVisibility();
}

function onClicked(id, divType, divName, which){
    let rank = id.charAt(0);
    let suit = id.charAt(1);
    for(var i=0;i<divType.flops.length;++i) {
        if(divType.flops[i].status) {
            divType.flops[i].status = false;
            appendCard(`#${divName}-`+ i, `${id}`, `${id}`+'.png');
            which[i] = id;
            appendCard(`#${suit}-${rank}`, 'back-image', 'Red_back.jpg');
            return true;
        }
    }
    return false; 
}

function appendCard(divID, picID, picRoute)
{
    $(`${divID}`).empty();
    $(`${divID}`).append(`<img id="${picID}" src="/static/assets/${picRoute}" />`);
}


function checkButtonVisibility(){
    for(var i=0;i<models.flops.length;++i) if(models.flops[i].status == true) return;
    for(var i=0;i<hands.flops.length;++i) if(hands.flops[i].status == true) return;
    if(clickedRange) $('#b-btn')[0].style.visibility = 'visible';
}



