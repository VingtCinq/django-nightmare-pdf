/*
marginsType Integer - Specifies the type of margins to use. Uses 0 for default margin, 1 for no margin, and 2 for minimum margin.
pageSize String - Specify page size of the generated PDF. Can be A3, A4, A5, Legal, Letter, Tabloid or an Object containing height and width in microns.
printBackground Boolean - Whether to print CSS backgrounds.
printSelectionOnly Boolean - Whether to print selection only.
landscape Boolean - true for landscape, false for portrait.
*/

var argvs = process.argv.slice(2);

var settings = {
  pageSize: 'A4',
  landscape: false,
  printBackground: true,
  marginsType: 1,
  timeout: 1000
};


/* ---- RAISE ERRORS BASED ON ARGVS LENGTH ----*/

if (argvs.length < 2) {
  console.log("You must supply an url and a filename");
  process.exit();
}

if (argvs.length > 12) {
  console.log("Too much arguments supplied");
  process.exit();
}

/* ---- VALIDATE INPUTS ----*/

function isValidPageSize(val) {
  var arr = ['A3', 'A4', 'A5', 'Legal', 'Letter', 'Tabloid'];
  if (arr.indexOf(val) > -1) {
    return val;
  } else {
    console.log(val + " is not a valid argument for pageSize, here are the valid ones : " + arr.join(' | '));
    process.exit();
  }
}

function isValidLandscape(val) {
  var arr = ['0', '1'];
  if (arr.indexOf(val) > -1) {
    return Boolean(parseInt(val));
  } else {
    console.log(val + " is not a valid argument for landscape, here are the valid ones : " + arr.join(' | '));
    process.exit();
  }
}

function isValidPrintBackground(val) {
  var arr = ['0', '1'];
  if (arr.indexOf(val) > -1) {
    return Boolean(parseInt(val));
  } else {
    console.log(val + " is not a valid argument for printBackground, here are the valid ones : " + arr.join(' | '));
    process.exit();
  }
}

function isValidMarginsType(val) {
  var arr = ['0', '1', '2'];
  if (arr.indexOf(val) > -1) {
    return parseInt(val);
  } else {
    console.log(val + " is not a valid argument for marginsType, here are the valid ones : " + arr.join(' | '));
    process.exit();
  }
}

function isValidTimeout(val) {
  if (isNaN(val)) {
    console.log(val + " is not a valid argument for Timeout. It must be a valid number");
    process.exit();
  } else {
    return parseInt(val);
  }
}

var validation = {
  pageSize: isValidPageSize,
  landscape: isValidLandscape,
  printBackground: isValidPrintBackground,
  marginsType: isValidMarginsType,
  timeout: isValidTimeout
}

/* ---- TRANSFORM ARGVS TO DICT ----*/

var currentOption = null;
var args = [];

function validateOption(arg) {
  settings[currentOption] = validation[currentOption](arg);
  currentOption = null;
}

function processArg(arg) {
  if ( arg.substring(0,2) == '--' ) { // The arg is a prefix like --timeout
    var option = arg.substring(2, arg.length); // Get the prefix, eg: timeout
    if ( Object.keys(validation).indexOf( option ) > -1 ) {
      currentOption = option;
    } else {
      console.log(arg + " is not a valid prefix");
      process.exit();
    }  
  } else {
    if (currentOption) {
      validateOption(arg);
    } else {
      args.push(arg);
    }
  }
}

argvs.map(function(arg) {
  processArg(arg);
});

if (args.length > 2) {
  console.log("Too much arguments supplied");
  process.exit();
}

var url = args[0];
var filename = args[1];


/* ---- LAUNCH NIGHTMARE PROCESS ----*/

var Nightmare = require('nightmare');

var nightmare = Nightmare({
  show: false,
  webPreferences: {
    partition: 'nopersist'
  }
});

nightmare
  .goto(url)
  .wait(settings.timeout)
  .pdf(filename, settings)
  .end()
  .then(function (result) {
    console.log(result);
  })
  .catch(function (error) {
    console.log(error);
  });
