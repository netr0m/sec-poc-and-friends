# Bitwarden `iframe` autofill

> Provides a basic PoC for exploiting the Bitwarden *design choice* to fill credentials in `<iframes />` on websites.

If a *Login* matching the current domain is found, the Bitwarden extension will fill in any `<input />` fields for username (i.e. username, email, etc) and password on the website, whether those `<input />` fields are *plain HTML* or inside an `<iframe />`. This applies to both the "Auto-fill on page load" feature and the manually triggered "Auto fill" feature (i.e. clicking the Login item in the Bitwarden extension popup). Another fun *feature* is the fact that the `<iframe />` can be hidden (using the `hidden` property on the `iframe` HTML element), meaning the user is likely to be unaware of the presence of this `iframe`.

Although this PoC runs both the "legitimate application" (i.e. [DonkeyApp](./donkeyapp/app.py)) and the evil application (i.e. [DefinitelyNotEvilApp](./definitelynotevilapp/app.py)) on the same domain (localhost), this will work even if they're running on different subdomains (such as web.myapp.com and evil.myapp.com), or on completely different domains (myapp.com and evil.io).

## The PoC
The *legitimate* website, [DonkeyApp](./donkeyapp/app.py), provides a simple login form, while the evil website, [DefinitelyNotEvilApp](./definitelynotevilapp/app.py), provides another login form which is inserted into `DonkeyApp` as an `<iframe />`. The `DefinitelyNotEvilApp` contains a script which is triggered when the *evil* form's inputs (email & password) changes. The values of these inputs are then extracted, base64 encoded, and sent to the `/capture` endpoint of the `DefinitelyNotEvilApp`.

When a user visits the *legitimate* website `DonkeyApp` and the auto-fill feature of the Bitwarden extension fills the *legitimate* login form on `DonkeyApp` (as expected), the Bitwarden extension will also auto-fill the login form in the `iframe` containing the *evil* `DefinitelyNotEvilApp`'s which in turn steals the credentials and sends them to the attacker.

## Running
```bash
$ docker compose up --build
```

1. Visit [http://localhost:8088](http://localhost:8088)
2. Use the Bitwarden extension to fill a Login for `localhost` (requires the presence of a Login for `localhost` in your account)
3. Check the logs of the `definitelynotevil` container
4. `$$$`

## Resources
- https://flashpoint.io/blog/bitwarden-password-pilfering/
