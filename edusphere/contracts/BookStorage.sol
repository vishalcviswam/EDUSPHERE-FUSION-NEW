// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BookStorage {
    struct Book {
        uint256 creatorId; // ID of the content creator
        string content; // Textual content of the book
    }

    mapping(uint256 => Book) public books; // Mapping to store books by an ID
    uint256 public lastBookId = 0; // Keep track of the last book ID to automatically assign new IDs

    event BookAdded(uint256 bookId, uint256 creatorId, string content); // Event to emit when a new book is added

    /**
     * @dev Adds a new book to the storage.
     * @param _creatorId The ID of the content creator.
     * @param _content The textual content of the book.
     */
    function addBook(uint256 _creatorId, string memory _content) public {
        lastBookId++; // Increment the book ID for each new book
        books[lastBookId] = Book(_creatorId, _content); // Store the new book

        emit BookAdded(lastBookId, _creatorId, _content); // Emit the event
    }

    /**
     * @dev Retrieves the details of a book by its ID.
     * @param _bookId The ID of the book to retrieve.
     * @return The ID of the content creator and the textual content of the book.
     */
    function getBook(uint256 _bookId) public view returns (uint256, string memory) {
        Book memory book = books[_bookId]; // Get the book from storage
        return (book.creatorId, book.content); // Return the book details
    }
}
