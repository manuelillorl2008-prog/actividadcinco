import reflex as rx


def navbar():

    return rx.hstack(

        rx.heading(
            "jive",
            font_size="2em",
            font_weight="bold",
        ),

        rx.spacer(),

        rx.link(

            rx.button(
                "Login",
                variant="outline",
                border_radius="25px",
                height="45px",
                padding_x="1.5em",
            ),

            href="/login",
        ),

        rx.link(

            rx.button(
                "Sign up",
                bg="black",
                color="white",
                border_radius="25px",
                height="45px",
                padding_x="1.5em",
            ),

            href="/signup",
        ),

        width="100%",
        align="center",
        padding_top="1.5em",
    )


def hero():

    return rx.vstack(

        rx.heading(
            "Don't make\nconnecting\nawkward",
            text_align="center",
            font_size="5em",
            line_height="1",
        ),

        rx.text(
            "No more fumbling for business cards or searching for lost contacts after an event.",
            text_align="center",
            color="gray",
            width="600px",
        ),

        rx.link(

            rx.button(
                "Sign up free",
                bg="black",
                color="white",
                border_radius="30px",
                padding_x="2em",
                padding_y="1.5em",
            ),

            href="/signup",
        ),

        spacing="6",
        align="center",
        padding_top="4em",
    )


def colorful_shapes():

    return rx.box(

        rx.box(
            bg="#ffb703",
            width="150px",
            height="70px",
            border_radius="50px",
            position="absolute",
            top="140px",
            left="-30px",
            transform="rotate(35deg)",
        ),

        rx.box(
            bg="#00c896",
            width="150px",
            height="70px",
            border_radius="50px",
            position="absolute",
            top="450px",
            left="70px",
            transform="rotate(-35deg)",
        ),

        rx.box(
            bg="#8b5cf6",
            width="150px",
            height="70px",
            border_radius="50px",
            position="absolute",
            top="550px",
            right="70px",
            transform="rotate(35deg)",
        ),

    )


def phones():

    return rx.center(

        rx.image(
            src="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c",
            width="450px",
            border_radius="25px",
            box_shadow="0px 15px 40px rgba(0,0,0,0.2)",
        ),

        padding="4em",
    )


def features():

    return rx.vstack(

        rx.heading(
            "Here's how it works",
            font_size="2.5em",
        ),

        rx.text(
            "More jiving, less shucking.",
            color="gray",
        ),

        rx.hstack(

            rx.vstack(
                rx.heading("Scan the QR code"),
                rx.text(
                    "Swap information quickly.",
                    text_align="center",
                ),
                align="center",
                width="250px",
            ),

            rx.vstack(
                rx.heading("Send a message"),
                rx.text(
                    "Connect instantly.",
                    text_align="center",
                ),
                align="center",
                width="250px",
            ),

            rx.vstack(
                rx.heading("Follow-up"),
                rx.text(
                    "Keep conversations going.",
                    text_align="center",
                ),
                align="center",
                width="250px",
            ),

            spacing="9",
            justify="center",
            width="100%",
        ),

        rx.link(

            rx.button(
                "Start Jiving",
                bg="black",
                color="white",
                border_radius="30px",
                margin_top="2em",
                padding_x="2em",
            ),

            href="/login",
        ),

        spacing="6",
        align="center",
        padding="5em",
    )


def footer():

    return rx.vstack(

        rx.heading("jive"),

        rx.text(
            "Get connected and start jiving.",
            color="gray",
        ),

        rx.hstack(
            rx.text("About"),
            rx.text("Privacy"),
            rx.text("Terms"),
            rx.text("Contact"),
            spacing="5",
        ),

        rx.text(
            "© 2026 Jive",
            color="gray",
            font_size="0.8em",
        ),

        spacing="4",
        padding="4em",
    )


def login_page():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Sign in",
                font_size="3em",
            ),

            rx.input(
                placeholder="Username",
                width="320px",
            ),

            rx.input(
                placeholder="Email",
                width="320px",
            ),

            rx.button(
                "Login",
                width="320px",
                bg="blue",
                color="white",
            ),

            rx.link(
                rx.text(
                    "Create an account",
                    color="blue",
                    cursor="pointer",
                ),
                href="/signup",
            ),

            spacing="4",
            padding="4em",
            bg="white",
            border_radius="25px",
            box_shadow="0px 15px 40px rgba(0,0,0,0.1)",
        ),

        height="100vh",
        bg="#f5f5f5",
    )


def signup_page():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Create account",
                font_size="3em",
            ),

            rx.input(
                placeholder="Name",
                width="320px",
            ),

            rx.input(
                placeholder="Email",
                width="320px",
            ),

            rx.input(
                placeholder="Password",
                type_="password",
                width="320px",
            ),

            rx.button(
                "Create account",
                width="320px",
                bg="black",
                color="white",
            ),

            spacing="4",
            padding="4em",
            bg="white",
            border_radius="25px",
            box_shadow="0px 15px 40px rgba(0,0,0,0.1)",
        ),

        height="100vh",
        bg="#f5f5f5",
    )


def index():

    return rx.center(

        rx.box(

            colorful_shapes(),

            rx.vstack(

                navbar(),

                hero(),

                phones(),

                features(),

                footer(),

                spacing="6",
                width="100%",
                align="center",
            ),

            width="100%",
            max_width="1200px",
            position="relative",
        ),

        bg="#f8f8f8",
        min_height="100vh",
        width="100%",
    )


app = rx.App()

app.add_page(index, route="/")

app.add_page(login_page, route="/login")

app.add_page(signup_page, route="/signup")