class AnimeFrameworkBoxExtension extends HTMLElement {
	  static #isAnimeFrameworkLoaded = false;
	  #break_orderd = true;

  	constructor() {
	    	super();
		    if (AnimeFramework.#isAnimeFrameworkLoaded) {
			      throw new Error("[AnimeFrameworkBoxExtension Error] <anime-framework-box-extension> component can loaded only once.");
		    }
		    AnimeFramework.#isAnimeFrameworkLoaded = true;
		    this.#break_orderd = false;
	  }
    
	  connectedCallback() {
		    if (this.#break_orderd) return;
		    this.innerHTML = `
<style>
	@import url("https://xunr3.github.io/ab.css");

	anime-framework-box-extension {
		display: block !important;
		width: 0 !important;
		height: 0 !important;
		overflow: hidden !important;
		visibility: hidden !important;
		pointer-events: none !important;
		user-select: none !important;
	}
</style>
		    `;

    		customElements.define('anime-box', AnimeBox);
	  }
}

customElements.define('anime-framework-box-extension', AnimeFrameworkBoxExtension);

const ab_webcode = (_ => console.log('<script src="https://xunr3.github.io/ab.js" fetchpriority="high"></script>'));

        class AnimeBox extends HTMLElement {
            #style = "";
            #class = "anime-box-class anime-box-input-target";
            #width = null;
            #height = null;
            #ALLOWattributeChangedCallback = null;
        
            connectedCallback() {
                setTimeout(() => {
                    if (this.width) this.#genSize(true, this.width);
                    if (this.height) this.#genSize(false, this.height);
                    if (this.animeInputTargeting) this.#changeStyle(false, true);
                    if (this.animeColoring) this.#changeStyle(true, true);
                    this.#changeStyle(null, false);
                    this.#appSize(false);
                    if (this.animeBoxBordering) this.#animeBoxBordering(true);
                    this.#ALLOWattributeChangedCallback = true;
                }, 0);
            }
        
            static get observedAttributes() {
                return ['width', 'height', 'anime-input-targeting', 'anime-box-bordering', 'anime-coloring'];
            }
        
            get animeInputTargeting() {
                return this.hasAttribute('anime-input-targeting');
            }
        
            set animeInputTargeting(val)  {
                if (val) {
                    this.setAttribute('anime-input-targeting', '');
                } else {
                    this.removeAttribute('anime-input-targeting');
                }
            }
        
            get animeBoxBordering() {
                return this.hasAttribute('anime-box-bordering');
            }
        
            set animeBoxBordering(val)  {
                if (val) {
                    this.setAttribute('anime-box-bordering', '');
                } else {
                    this.removeAttribute('anime-box-bordering');
                }
            }
        
            get animeColoring() {
                return this.hasAttribute('anime-coloring');
            }
        
            set animeColoring(val)  {
                if (val) {
                    this.setAttribute('anime-coloring', '');
                } else {
                    this.removeAttribute('anime-coloring');
                }
            }
        
            get width() {
                if (!this.hasAttribute('width')) return;
                return this.getAttribute('width');
            }
        
            set width(value) {
                this.setAttribute('width', value);
            }
        
            get height() {
                if (!this.hasAttribute('height')) return;
                return this.getAttribute('height');
            }
        
            set height(value) {
                this.setAttribute('height', value);
            }
        
            attributeChangedCallback(name, oldValue, newValue) {
                if (this.#ALLOWattributeChangedCallback) {
                    let flag = false;
                    switch (name) {
                        case 'width':
                            flag = true;
                            /* falls through */
                        case 'height':
                            if (oldValue || newValue) {
                                if (flag) {
                                    this.#delSize(flag);
                                } else if (newValue) {
                                    this.#genSize(flag, newValue);
                                } else if (oldValue !== newValue) {
                                    this.#setSize(flag, newValue);
                                }
                                this.#appSize(this.animeBoxBordering);
                            }
                            break;
                      case 'anime-coloring':
                          flag = true;
                          /* falls through */
                      case 'anime-input-targeting':
                          if (oldValue || newValue) {
                              if ((!oldValue) && newValue) {
                                  this.#changeStyle(flag, true);
                              } else if ((!newValue) && oldValue) {
                                  this.#changeStyle(flag, false);
                              }
                              this.#changeStyle(null, this.animeBoxBordering);
                          }
                          break;
                      case 'anime-box-bordering':
                          if ((!oldValue) && newValue) {
                              this.#animeBoxBordering(true);
                          } else if ((!newValue) && oldValue) {
                              this.#animeBoxBordering(false);
                          }
                          break;
                    }
                }
            }
        
            #animeBoxBordering(dose_it) {
                if (this.#ALLOWattributeChangedCallback !== null) this.#ALLOWattributeChangedCallback = false;
                if (dose_it) {
                    const boxBorder = Object.assign(document.createElement('fieldset'), {className: this.#class, innerHTML: this.innerHTML});
                    this.removeAttribute("class");
                    
                    if (this.#style) {
                        Object.assign(boxBorder.style, {cssText: this.#style})
                        this.removeAttribute("style");
                    }
        
                    this.innerHTML = "";
                    this.appendChild(boxBorder);
                } else {
                    const boxBorder = this.querySelector("fieldset");
                    if (this.#style) this.setAttribute("style", this.#style);
                    this.setAttribute("class", this.#class);
                    this.innerHTML = boxBorder.innerHTML;
                }
                if (this.#ALLOWattributeChangedCallback !== null) this.#ALLOWattributeChangedCallback = true;
            }
        
            #changeStyle(mode, argument) {
                if (mode === null) {
                    if (this.#ALLOWattributeChangedCallback !== null) this.#ALLOWattributeChangedCallback = false;
                    (argument?this.querySelector("fieldset"):this).setAttribute("class", this.#class);
                    if (this.#ALLOWattributeChangedCallback !== null) this.#ALLOWattributeChangedCallback = true;
                } else if (mode) { //it's doColoring mode bool
                    if (argument) {
                        this.#class = this.#class.replace(`anime-box-${this.animeInputTargeting?"anime-":""}input-target`, `anime-box-coloringed-${this.animeInputTargeting?"anime-":""}input-target`);
                    } else {
                        this.#class = this.#class.replace(`anime-box-coloringed-${this.animeInputTargeting?"anime-":""}input-target`, `anime-box-${this.animeInputTargeting?"anime-":""}input-target`);
                    }
                } else {
                    if (argument) {
                        this.#class = this.#class.replace("anime-box-input-target", "anime-box-anime-input-target");
                    } else {
                        this.#class = this.#class.replace("anime-box-anime-input-target", "anime-box-input-target");
                    }
                }
            }
        
        
        
            #delSize(is_width) {
                if (is_width) {
                    this.#style = this.#style.replace(`--anime-box-width: ${this.#width};`, "");
                    this.#width = null;
                } else {
                    this.#style = this.#style.replace(`--anime-box-height: ${this.#height};`, "");
                    this.#height = null;
                }
            }
        
            #genSize(is_width, value) {
                if (is_width) {
                    this.#style += `--anime-box-width: ${value};`;
                    this.#width = value;
                } else {
                    this.#style += `--anime-box-height: ${value};`;
                    this.#height = value;
                }
            }
        
            #setSize(is_width, value) {
                if (is_width) {
                    this.#style = this.#style.replace(`th: ${this.#width}`, `th: ${value}`);
                    this.#width = value;
                } else {
                    this.#style = this.#style.replace(`ht: ${this.#height}`, `ht: ${value}`);
                    this.#height = value;
                }
            }
        
            #appSize(isBoxBordered) {
                if (this.#ALLOWattributeChangedCallback !== null) this.#ALLOWattributeChangedCallback = false;
                const elem = isBoxBordered?this.querySelector("fieldset"):this;
                if (this.#style) {
                    elem.setAttribute("style", this.#style);
                } else {
                    if (elem.hasAttribute("style")) elem.removeAttribute("style");
                }
                if (this.#ALLOWattributeChangedCallback !== null) this.#ALLOWattributeChangedCallback = true;
            }
        }