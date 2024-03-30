describe('Login Test', () => {
    it('Unsuccessful login', () => {
        cy.visit('http://localhost:8000/')

        cy.get('input[name="username"]')
          .type('FakeName')
        cy.wait(500); // Just for learning purposes, this would not be here in production

        cy.get('input[name="password"]')
          .type('FakePassword')
        cy.wait(500); // Just for learning purposes, this would not be here in production

        cy.get('button[type="submit"]').click();
        cy.wait(500); // Just for learning purposes, this would not be here in production

        // Adjust this to check for something specific on the page after login
        cy.contains('Try here, credentials were not valid.')
    })
    it('Successful login', () => {
        cy.visit('http://localhost:8000/')

        cy.get('input[name="username"]')
          .type('pablo')
        cy.wait(500); // Just for learning purposes, this would not be here in production

        cy.get('input[name="password"]')
          .type('1234')
        cy.wait(500); // Just for learning purposes, this would not be here in production

        cy.get('button[type="submit"]').click();
        cy.wait(500); // Just for learning purposes, this would not be here in production

        // Adjust this to check for something specific on the page after login
        cy.contains('Welcome, pablo!')
    })
})
