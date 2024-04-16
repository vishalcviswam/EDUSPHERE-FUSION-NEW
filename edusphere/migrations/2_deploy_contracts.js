const BookStorage = artifacts.require("BookStorage");

module.exports = function(deployer) {
    deployer.deploy(BookStorage);
};
