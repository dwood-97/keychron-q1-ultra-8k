- **Layers/modes**: one button changes the meaning of every other button.
- **Tap / hold / double-tap / triple-tap behaviors**.
- **Chords**: G4+G5 means something different from either button alone.
- **Stateful toggles**: “Mode A / Mode B / Mode C.”
- **Timed sequences**: one input causes a series of delayed keystrokes.
- **Repeat-while-held behavior**.
- **Conditional macros** based on Caps Lock / Num Lock / Scroll Lock state.
- **Per-profile behavior**, so the same physical button behaves differently by application.
- **Pseudo-combo engines**, where successive presses advance through steps.
- **Cross-device modifier systems**, e.g. Keychron layer key changes how G502 inputs are interpreted.
- **Input logging/debugging**, including timestamps.
- **Randomization/jitter** for testing UI behavior.
- **Mouse movement scripts**, clicks, drag sequences, etc.
- **Launch apps / open URLs / type command strings**.
- **Whole desktop workflows** like opening terminals, typing commands, moving windows, and switching profiles.

The really fun part is **state**.

For example, conceptually your G502 Lua could behave like this:

```lua
mode = 1
comboStep = 1

function OnEvent(event, arg)
    if event == "PROFILE_ACTIVATED" then
        mode = 1
        comboStep = 1
        OutputLogMessage("Profile initialized\n")
    end

    if event == "MOUSE_BUTTON_PRESSED" then

        -- Button 8 cycles modes
        if arg == 8 then
            mode = mode + 1

            if mode > 3 then
                mode = 1
            end

            OutputLogMessage("Mode = %d\n", mode)
        end

        -- Button 4 behaves differently in each mode
        if arg == 4 then

            if mode == 1 then
                PressAndReleaseKey("f13")

            elseif mode == 2 then
                PressAndReleaseKey("f14")

            elseif mode == 3 then
                PressAndReleaseKey("f15")
            end
        end
    end
end
```

Now one mouse button effectively represents **three different inputs**.

You could take that further and use **Scroll Lock as a global hardware mode**:

```lua
function OnEvent(event, arg)

    if event == "MOUSE_BUTTON_PRESSED" and arg == 4 then

        if IsKeyLockOn("scrolllock") then
            PressAndReleaseKey("f13")
        else
            PressAndReleaseKey("f1")
        end

    end
end
```

So:

```text
Scroll Lock OFF
G4 → F1

Scroll Lock ON
G4 → F13
```

That means your keyboard can control the mouse's logical layer without the devices actually talking directly.

## Then you can make a combo state machine

This is where it starts feeling like actual software rather than macros.

Imagine pressing the same button repeatedly:

```lua
step = 1

function OnEvent(event, arg)

    if event == "MOUSE_BUTTON_PRESSED" and arg == 5 then

        if step == 1 then
            PressAndReleaseKey("f13")
            step = 2

        elseif step == 2 then
            PressAndReleaseKey("f14")
            step = 3

        elseif step == 3 then
            PressAndReleaseKey("f15")
            step = 1
        end

    end
end
```

For experimenting outside WoW, bind F13/F14/F15 to something visible in a test program and you get:

```text
press 1 → action A
press 2 → action B
press 3 → action C
press 4 → action A
```

You could even reset that state after a timeout.

```lua
step = 1
lastPress = 0

function OnEvent(event, arg)

    if event == "MOUSE_BUTTON_PRESSED" and arg == 5 then

        local now = GetRunningTime()

        if now - lastPress > 3000 then
            step = 1
        end

        lastPress = now

        if step == 1 then
            PressAndReleaseKey("f13")
            step = 2

        elseif step == 2 then
            PressAndReleaseKey("f14")
            step = 3

        else
            PressAndReleaseKey("f15")
            step = 1
        end
    end
end
```

That is essentially a tiny finite-state machine.

## Tap versus long press

You can also measure how long a mouse button is held.

Conceptually:

```lua
pressTime = 0

function OnEvent(event, arg)

    if arg == 4 and event == "MOUSE_BUTTON_PRESSED" then
        pressTime = GetRunningTime()
    end

    if arg == 4 and event == "MOUSE_BUTTON_RELEASED" then

        local heldFor = GetRunningTime() - pressTime

        if heldFor < 250 then
            PressAndReleaseKey("f13")
        else
            PressAndReleaseKey("f14")
        end

    end
end
```

Now:

```text
tap G4
→ F13

hold G4
→ F14
```

You can imagine where that goes.

Add double taps:

```text
single tap
double tap
hold
```

and one button has **three functions**.

Combine that with modes and suddenly one physical button could theoretically represent:

```text
3 modes
×
3 gestures
=
9 logical commands
```

Five programmable mouse buttons gives you 45 logical commands before even involving Shift/Ctrl/Alt.

## Chording gets even nerdier

You could track multiple button states:

```lua
g4Down = false
g5Down = false

function OnEvent(event, arg)

    if arg == 4 then
        g4Down = event == "MOUSE_BUTTON_PRESSED"
    end

    if arg == 5 then
        g5Down = event == "MOUSE_BUTTON_PRESSED"
    end

    if g4Down and g5Down then
        OutputLogMessage("G4 + G5 chord detected\n")
    end

end
```

Conceptually:

```text
G4        → action A
G5        → action B
G4 + G5   → action C
```

It's basically implementing your own miniature keyboard firmware in Lua.

## Repeat engines

Technically, Lua environments like this can also do things along the lines of:

```text
while button held:
    press key
    wait
    press key
    wait
```

For example, for testing a program:

```lua
while IsMouseButtonPressed(4) do
    PressAndReleaseKey("a")
    Sleep(100)
end
```

Hold G4 and you'd get:

```text
aaaaaaaaaaaaaaaaaaaaaaaa
```

That's exactly the type of capability that becomes problematic when applied to gameplay automation, but as an input-programming experiment it's interesting.

## Sequences

Likewise, you could make a desktop test macro:

```lua
PressAndReleaseKey("h")
Sleep(100)

PressAndReleaseKey("e")
Sleep(100)

PressAndReleaseKey("l")
Sleep(100)

PressAndReleaseKey("l")
Sleep(100)

PressAndReleaseKey("o")
```

One click:

```text
hello
```

Or much more complicated sequences involving modifiers:

```lua
PressKey("lctrl")
PressAndReleaseKey("l")
ReleaseKey("lctrl")

Sleep(200)

PressAndReleaseKey("h")
PressAndReleaseKey("e")
PressAndReleaseKey("l")
PressAndReleaseKey("l")
PressAndReleaseKey("o")

PressAndReleaseKey("enter")
```

In a browser that could focus the address bar, type something, and execute it.

That's where you start building actual **workflow automation**.

---

# The Keychron side is arguably even crazier

Especially if your board supports QMK-style configuration.

You've already used:

```qmk
MT(MOD_LCTL, KC_CAPS)
```

which is itself a little state machine:

```text
tap Caps
→ Caps Lock

hold Caps
→ Ctrl
```

But QMK can go much farther.

You can have:

```qmk
LT(2, KC_TAB)
```

meaning:

```text
tap
→ Tab

hold
→ Layer 2
```

Then Layer 2 could remap half your keyboard.

For example:

```text
NORMAL

Q W E R T
A S D F G
Z X C V B
```

becomes:

```text
LAYER 2

F13 F14 F15 F16 F17
F18 F19 F20 F21 F22
F23 F24 Home End Insert
```

One hold key suddenly creates an entire alternate keyboard.

## You can stack layers too

You could conceptually have:

```text
Layer 0
Normal typing

Layer 1
WoW

Layer 2
Development

Layer 3
Media

Layer 4
Window management
```

Then something like:

```text
Caps hold → Ctrl

Tab hold → WoW layer

Right Alt hold → development layer

Fn → media layer
```

Your development layer could be awesome:

```text
H → git status
J → git diff
K → git log --oneline
L → clear

U → kubectl get pods
I → terraform plan
O → terraform apply
```

Obviously I'd be careful with something like `terraform apply` 😂, but you get the idea.

## Tap dance

QMK supports the general idea of **tap dance**, where the number/type of presses matters.

You could have:

```text
tap once
→ Escape

tap twice
→ ~

hold
→ Ctrl

double tap + hold
→ Layer 3
```

At that point you're basically inventing your own input language.

---

# The truly absurd setup

Here's what I'd build purely for the engineering amusement.

Your **Keychron controls global modes**:

```text
Caps hold
→ Ctrl

Tab hold
→ WoW Layer

Right Alt hold
→ Dev Layer

Scroll Lock
→ toggle G502 alternate mode
```

Then the **G502 interprets those states**.

For instance:

```text
G502 MODE 1

G8 → F13
G7 → F14
G5 → F15
G4 → F16
DPI → F17
```

Toggle Scroll Lock:

```text
G502 MODE 2

G8 → F18
G7 → F19
G5 → F20
G4 → F21
DPI → F22
```

Then combine Shift:

```text
Shift + G8 → F23
Shift + G7 → F24
...
```

And gesture detection:

```text
G4 tap
G4 hold
G4 double tap
```

You could conceivably turn **five mouse buttons into dozens of distinct logical inputs**.

And the hilarious thing is that Windows would simply see:

```text
F13
F19
F22
Ctrl+F17
...
```

It wouldn't know or care that you have a bizarre two-device input architecture behind it.

---

## Where I'd take this as a software project

Rather than making a WoW automation script, I'd actually build a little **input laboratory**.

Have the G502 output things like:

```text
F13-F24
```

and write a tiny Python/JavaScript app showing:

```text
Input: F17
Mode: Combat
Button: G5
Gesture: Hold
Duration: 437ms
Previous input: F13
Time since previous: 829ms
```

Then you could experiment with:

**gesture detection → state machine → logical action**

without risking your WoW account at all.

That would actually be a pretty fun weekend project, and given that you work in DevOps/software, you'd probably end up with something hilariously overengineered like:

```text
G502
   ↓
Logitech Lua
   ↓
F13-F24 virtual input layer
   ↓
Python event listener
   ↓
state machine
   ↓
profiles/config YAML
   ↓
OS actions
```