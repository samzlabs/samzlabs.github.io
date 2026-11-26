# LanGuard Pro privacy policy

Effective: 23 October 2026

LanGuard Pro is local-first network-management software. It does not serve
advertising or send analytics to SAMZLAB-PK. Router-management data is obtained
directly from the router the user configures. The router stores network device
identifiers, IP addresses, user-assigned names, online status, traffic totals and
policies in `/etc/languard-pro/usage.db`. The Android app stores user-supplied
router profiles in local application/WebView storage. A user may choose to save a
router password for a profile or keep it only in session storage. Optional install,
update, repair and uninstall operations use the selected router's SSH connection.
Demo Mode uses simulated data and does not contact a router or read saved router
credentials.

## Firebase trial verification

The optional seven-day Plus/Pro trial uses Firebase Authentication (anonymous
sign-in) and Firebase Realtime Database. To reduce repeated-trial resets, the app
reads Android's `Settings.Secure.ANDROID_ID`, computes a SHA-256 hash on the device,
and uses the hash as the key for its cloud trial record. The trial record contains
the selected plan tier (`plus` or `pro`), original start timestamp, expiry
timestamp, and schema version. Firebase server-time offset is used to calculate
remaining time. The raw Android ID is not written as the key for new records; for
one-time compatibility migration only, the app may read an earlier-format record
under the raw-ID path. The Firebase database is hosted in the configured
`asia-southeast1` region.

This record is retained after the local app cache is cleared so reinstalling or
clearing app storage does not grant a new seven-day trial. Switching between Plus
and Pro during an active trial changes only the selected tier, not the original
start or expiry. The database owner can administratively remove records; normal
app-client rules do not allow trial-record deletion. Android ID is an app-scoped
device identifier and is not a permanent hardware serial number.

## Purchases

Lifetime Plus, Lifetime Pro and the Plus-to-Pro upgrade are optional one-time
in-app products handled by Google Play Billing. Google Play processes payments and
provides purchase information to the app. The app displays prices returned by
Google Play for the user's region. LanGuard Pro does not collect card numbers or
other payment credentials.

## Storage, control and deletion

Clearing Android application storage removes local settings and cached data but
does not remove the Firebase trial record. Users can remove locally stored router
profiles through the app and can remove router history from the router using the
provided router-management tools. Normal router companion uninstall preserves the
router database to prevent accidental history loss; a documented purge operation
removes router runtime data.

Do not expose the router API to the public internet. Do not send router passwords, tokens, device databases or private network details with a bug report.

## Contact

SAMZLAB - samzlabpk@gmail.com
