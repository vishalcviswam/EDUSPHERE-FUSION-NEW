// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BookData {
    struct Book {
        uint256 creatorId; 
        string content;
    }

    mapping(uint256 => Book) public books;
    uint256 public lastBookId = 0;

    event BookAdded(uint256 bookId, uint256 creatorId, string content);

    function addBook(uint256 _creatorId, string memory _content) public returns (uint256) {
    lastBookId++;
    books[lastBookId] = Book(_creatorId, _content);
    emit BookAdded(lastBookId, _creatorId, _content);
    return lastBookId;
    }


    function getBook(uint256 _bookId) public view returns (uint256, string memory) {
        Book memory book = books[_bookId]; 
        return (book.creatorId, book.content);
    }
}
