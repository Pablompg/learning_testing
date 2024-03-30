import { fireEvent, render, screen } from '@testing-library/vue'
import Login from '../../src/components/Login.vue'
import userEvent from '@testing-library/user-event'
import { useRouter } from 'vue-router'


// Mock the vue-router module
vi.mock('vue-router', () => ({
  useRouter: vi.fn().mockReturnValue({
    push: vi.fn(),
  })
}));

describe('Login tests', () => {

  it('renders properly with button disabled when there is no input in email and password', async () => {
    render(Login)

    // Assert Email and Password are present
    expect(await screen.findByText('Email:')).toBeVisible()
    expect(await screen.findByText('Password:')).toBeVisible()

    // Assert that the button is disabled
    const loginButton = await screen.findByRole('button')
    expect(loginButton).toBeDisabled()
  })

  it('should enable login button when email and password are filled', async () => {
    const { findByLabelText, findByRole } = render(Login)

    // Find input fields
    const emailInput = await findByLabelText('Email:')
    const passwordInput = await findByLabelText('Password:')

    // Type into the input fields
    await userEvent.type(emailInput, 'user@example.com')
    await userEvent.type(passwordInput, 'password')

    // Assert that the button is enabled
    const loginButton = await findByRole('button')
    expect(loginButton).toBeEnabled()
  })

  it('should use router to redirect to welcome page when submitting form', async () => {
    const { findByLabelText, findByRole } = render(Login)

    // Find input fields
    const emailInput = await findByLabelText('Email:')
    const passwordInput = await findByLabelText('Password:')

    // Type into the input fields
    await userEvent.type(emailInput, 'user@example.com')
    await userEvent.type(passwordInput, 'password')

    // Click submit button
    const loginButton = await findByRole('button')
    await fireEvent.click(loginButton)

    // Assert router.push was called correctly
    const router = useRouter()
    expect(router.push).toHaveBeenCalledWith({
      path: '/welcome',
      query: { email: 'user@example.com' },
    })
  })
})
