import {Flop, Models} from './createModels.js';
const navBarHeight = 70;
const models = new Models();
const split = window.location.href.split('?');
const whichFlop = [split[4], split[5], split[6]];


$(document).ready(function() {
    initLayout();
    initFlop();
});

function initLayout() {
    var winHeight = window.innerHeight;
    setContainerHeight(winHeight - navBarHeight);
    window.onresize = reportWindowSize;
    initPositions();
    var keys = setKeyValues();
    setMid(keys); 
    setPercentage(keys, firstRange, 'pos1');
    setPercentage(keys, secondRange, 'pos2');
    manageInputData(); 
}

function reportWindowSize(){ setContainerHeight(window.innerHeight - navBarHeight); }

function setContainerHeight(height) { $('#c-container').height(height + 'px'); }

function initPositions()
{

    document.getElementById("pos_name").textContent += split[1] + ': ' + split[2] + ' vs ' + split[3];
    document.getElementById("first_pos").textContent += split[2];
    document.getElementById("second_pos").textContent += split[3];
}
function manageInputData()
{
    $('#reselect').click(function() { window.location.replace('findFlop' +'?' + split[1] + '?'+ split[2] + '?'+ split[3]); })
    $('#range').click(function() { window.location.replace('ranges'); })
}
function initFlop() 
{
    for(var i=0;i<3;++i) {
        var flop = new Flop();
        var card = whichFlop[i];
        flop.imgDiv = $('#flop-' + i).append(`<img src="/static/assets/${card}.png" />`);
        models.flops.push(flop);
    }
}

function setMid(arr) {
    for (var idx = 0; idx < arr.length; idx++) { 
        var element = document.getElementById("msg");
        var tag = document.createElement("h5");
        if (arr[idx] == 'BREAK'){
            element.appendChild(document.createElement('br'));
            continue;
        }
        var text = document.createTextNode(arr[idx]);
        tag.appendChild(text);
        element.appendChild(tag);
    } 
}

function setPercentage(arr, res, pos) {
    for (var idx = 0; idx < arr.length; idx++) {
        var element = document.getElementById(pos);
        var tag = document.createElement("h5");
        if (arr[idx] == 'BREAK'){
            element.appendChild(document.createElement('br'));
            continue;
        }
        var text = document.createTextNode(res[arr[idx]]);
        tag.appendChild(text);
        element.appendChild(tag);
      }
}

function setKeyValues()
{  
    var keys = [];
    // 3 tone connected 
    if(flopClass == '1'){
        keys = ['Nuts', 'BREAK',
        'All Pairs', 'BREAK',
        'Top Pair+','BREAK',
        'Overpairs','BREAK',
        'Strong Top Pairs','BREAK',
        'Strong Middling Pairs','BREAK',
        'Strong Bottom Pairs','BREAK',
        'All Straight Draws','BREAK',
        'Open-Ended Straight Draws','BREAK',
        'Pairs with Straight Draws','BREAK',
        'Top Pairs with Straight Draws','BREAK',
        'Middling Pairs with Straight Draws','BREAK',
        'All BDFDs','BREAK',
        'BDFDs with Straight Draws','BREAK',
        'BDFDs with 2 overcards','BREAK',
        'BDFDs with 1 overcard','BREAK',
        'BDFDs with Pairs','BREAK'
        ]; 
    }

    // 2 tone connected 
    else if(flopClass == '2'){
        keys = ['Nuts', 'BREAK',
        'All Pairs', 'BREAK',
        'Top Pair+','BREAK',
        'Overpairs','BREAK',
        'Strong Top Pairs','BREAK',
        'Strong Middling Pairs','BREAK',
        'Strong Bottom Pairs','BREAK',
        'All Flush Draws', 'BREAK',
        'Nut Flush Draws','BREAK',
        'Straight and Flush Draws','BREAK',
        'Pairs with Flush Draws','BREAK',
        'All Straight Draws','BREAK',
        'Open-Ended Straight Draws','BREAK',
        'Pairs with Straight Draws','BREAK',
        'Top Pairs with Straight Draws','BREAK',
        'Middling Pairs with Straight Draws','BREAK',
        'BDFDs with Straight Draws','BREAK'
        ]; 
    }

    // 3 tone disconnected 
    else if(flopClass == '3'){
        keys = ['Nuts','BREAK',
        'All Pairs','BREAK',
        'Top Pair+','BREAK',
        'Overpair','BREAK',
        'Strong Top Pairs','BREAK',
        'Middling Top Pairs','BREAK',
        'Weak Top Pairs','BREAK',
        'Strong Middling Pairs','BREAK',
        'Strong Bottom Pairs','BREAK',
        'All Straight Draws','BREAK',
        'Open-Ended Straight Draws','BREAK',
        'All BDFDs','BREAK',
        'BDFDs with Straight Draws','BREAK',
        'BDFDs with 2 overcards','BREAK',
        'BDFDs with 1 overcard','BREAK',
        'BDFDs with Pairs','BREAK'
        ]; 
    }

    // 2 tone disconnected 
    else if(flopClass == '4'){
        keys = ['Nuts','BREAK',
        'All Pairs','BREAK',
        'Top Pair+','BREAK',
        'Overpairs','BREAK',
        'Strong Top Pairs','BREAK',
        'Middling Top Pairs','BREAK',
        'Weak Top Pairs','BREAK',
        'Strong Middling Pairs','BREAK',
        'Strong Bottom Pairs','BREAK',
        'All Flush Draws','BREAK',
        'Nut Flush Draws','BREAK',
        'Straight and Flush Draws','BREAK',
        'Pairs with Flush Draws','BREAK',
        'Flush Draws with 2 Overcards','BREAK',
        'Flush Draws with 1 Overcard','BREAK',
        'All Straight Draws','BREAK',
        'Open-Ended Straight Draws','BREAK'
        ]; 
    }

    // monotone 
    else if(flopClass == '5'){
        keys = ['Nuts','BREAK',
        'All Pairs','BREAK',
        'Top Pair+ with Flush Draws','BREAK',
        'Middling Pairs with Flush Draws','BREAK',
        'Bottom Pairs with Flush Draws','BREAK',
        'Top Pair+ with NO Flush Draws','BREAK',
        'Midding Pairs with NO Flush Draws','BREAK',
        'Bottom Pairs with NO Flush Draws','BREAK',
        'All Flush Draws','BREAK',
        'Nut Flush Draw (NO Pair)','BREAK',
        'Strong Flush Draw (NO Pair)','BREAK',]; 
        'Pairs with Nut Flush Draws','BREAK',
        'Pairs with Strong Flush Draws','BREAK'
    }

    
    // 3 tone paired 
    else if(flopClass == '6'){
        keys = ['Nuts','BREAK',
        'All Pairs','BREAK',
        'OverPairs','BREAK',
        'Strong Pairs on Board','BREAK',
        'Weak Pairs on Board','BREAK',
        'All BDFDs','BREAK',
        'BDFDs with 2 overcards','BREAK',
        'BDFDs with 1 overcard','BREAK',
        'BDFDs with Pairs','BREAK'
        ]; 
    }

    // 2 tone paired 
    else if(flopClass == '7'){
        keys = ['Nuts','BREAK',
        'All Pairs','BREAK',
        'Overpairs','BREAK',
        'Strong Pairs on Board','BREAK',
        'Weak Pairs on Board','BREAK',
        'Pairs with BDFDs','BREAK',
        'All Flush Draws','BREAK',
        'Nut Flush Draws','BREAK',
        'Pairs with Flush Draws','BREAK',
        'Flush Draws with 2 overcards','BREAK',
        'Flush Draws with 1 overcard','BREAK'
        ]; 
    }

    // 3 same card
    else{
        keys = ['Nuts','BREAK',
        'All Pairs','BREAK',
        'Overpairs','BREAK',
        'Underpairs','BREAK',
        '2 Overcards','BREAK',
        '1 Overcard','BREAK']; 
    }
    return keys 
}