This is an application to demonstrate how components interact with each others.

*Kiosk* is a service with three APIs, and it connect to a *redis* to cache its tickets. Tickets are set to zero by default, and they can be set with `POST /tickets`:
```
$ curl -XPOST -F 'value=10' <kiosk-service>/tickets
```
Our kiosk now can start its business. Use `GET /tickets` to know how many tickets left, And use `POST /buy` to consume one ticket.

```
// Get tickets
$ curl -XGET <kiosk-service>/tickets
// Buy one ticket
$ curl -XPOST <kiosk-service>/buy
```
