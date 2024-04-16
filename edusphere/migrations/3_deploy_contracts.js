const BookData = artifacts.require("BookData");

module.exports = function(deployer) {
    deployer.deploy(BookData, { gas: 5000000 });
};
