# OctoPrint-USBPowerControl (alpha version)

Disable USB power on serial disconnect, re-enable on connect.

Otherwise the Raspberry Pi will half-assedly power the Ender 3 with only LCD working faintly.

**WARNING** This will power down all 4 USB ports and even the Ethernet port!

**TODO** doesnt work very well yet, serial port needs to be set to Auto and it takes 2 clicks on Connect to 
connect to the printer because the TTY device disappears when the USB power is cut off.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/ozgunawesome/OctoPrint-USBPowerControl/archive/master.zip

## Configuration

No configuration required.

**TODO** give at least some configurability to the end user.

## Mandatory warnings

**THIS IS NOT PRODUCTION READY!!!!** Your house might go up in flames at any given moment.

#### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
