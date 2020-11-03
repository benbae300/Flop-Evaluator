import {Flop, Models} from './createModels.js';
const navBarHeight = 70;
const whichFlop = ['0', '0', '0'];
const cardRank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'];
const split = window.location.href.split('?');
const models = new Models();;


$(document).ready(function() 
{
    initLayout();
    initCards();
});

function initLayout() {
    var winHeight = window.innerHeight;
    setContainerHeight(winHeight - navBarHeight);
    window.onresize = reportWindowSize;
    manageInputData();
}

function initCards() {
    initFlop();
    setDeck('S');
    setDeck('C');
    setDeck('D');
    setDeck('H');
    monitorUserClick();
}

function reportWindowSize(){ setContainerHeight(window.innerHeight - navBarHeight); }

function setContainerHeight(height) {  $('#c-container').height(height + 'px'); }

function manageInputData()
{
    $('#b-btn')[0].style.visibility = 'hidden';
    document.getElementById("which_flop").textContent += split[1] + ': ' + split[2] + ' vs ' + split[3];
    $('#myButton').click(function() {window.location.replace('data?' + split[1] + '?'+ split[2] + '?'+ split[3] + '?'+whichFlop[0] + '?' + whichFlop[1]+ '?' + whichFlop[2]); })
}

function initFlop(){
    for(var i=0;i<3;++i){
        var flop = new Flop();
        $('#flop-' + i).append(`<img id="back-image" src="/static/assets/Red_back.jpg"/>`);
        models.flops.push(flop);
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
    $(document).on("click", ".b-flop", function(event) 
    {
        var id = event.target.id;
        if (id.length > 3) return; 
        var cardID = $(this).attr('id');
        onFlopClicked(cardID.split('-')[1], id);
        $('#b-btn')[0].style.visibility = 'hidden';
    })

    $(document).on("click", ".deck-card", function(event) 
    {
        var id = event.target.id;
        if (id.length > 2) return; 
        onCardClicked(id);
        for(var i=0;i<models.flops.length;++i) if(models.flops[i].status == true) return;
        $('#b-btn')[0].style.visibility = 'visible';

    })
}

function onFlopClicked(num, id) 
{
    var rank = id.charAt(0);
    var suit = id.charAt(1);
    appendCard('#flop-'+ num, 'back-image', 'Red_back.jpg'); 
    appendCard(`#${suit}-${rank}`, `${id}`, `${id}`+'.png');
    models.flops[parseInt(num)].status = true;

}

function onCardClicked(id) 
{
    var rank = id.charAt(0);
    var suit = id.charAt(1);
    for(var i=0;i<models.flops.length;++i) {
        if(models.flops[i].status) {
            models.flops[i].status = false;
            whichFlop[i] = id;
            appendCard('#flop-'+ i, `${id}`, `${id}`+'.png'); 
            appendCard(`#${suit}-${rank}`, 'back-image', 'Red_back.jpg');
            return;
        }
    }
}

function appendCard(divID, picID, picRoute)
{
    $(`${divID}`).empty();
    $(`${divID}`).append(`<img id="${picID}" src="/static/assets/${picRoute}" />`);
}




