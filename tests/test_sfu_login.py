import pytest

from upass.exceptions import InvalidCredentialsError
from upass.pages import SfuLoginPage

# Simulate MFA redirect upon successful login
LOGIN = """
<input id="username">
<input id="password" type="password">
<button name="submit" onclick="attempt()">Login</button>
<script>
function attempt() {
  const ok = document.getElementById('username').value === 'good'
          && document.getElementById('password').value === 'secret';
  setTimeout(() => {                      // simulate server latency
    if (ok) {
      const f = document.createElement('iframe');
      f.id = 'duo_iframe';
      document.body.appendChild(f);
    } else {
      const d = document.createElement('div');
      d.className = 'alert alert-danger';
      d.textContent = 'Invalid credentials';
      document.body.appendChild(d);
    }
  }, 100);
}
</script>
"""

@pytest.fixture
def load(driver, tmp_path):
    f = tmp_path / "page.html"
    f.write_text(LOGIN)
    driver.get(f.as_uri())
    return SfuLoginPage(driver, timeout=2)

def test_valid_login(load, driver):
    load.login("good", "secret")
    assert driver.find_elements("id", "duo_iframe")

def test_invalid_username(load):
    with pytest.raises(InvalidCredentialsError):
        load.login("bad", "secret")


def test_invalid_password(load):
    with pytest.raises(InvalidCredentialsError):
        load.login("good", "bad")