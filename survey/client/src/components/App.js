import React from 'react';
import BaseComponent from "./base/BaseComponent";
import SideNavbar from './common/SideNavbar'
import TopNavbar from './common/TopNavbar'

class App extends BaseComponent {
    constructor(props) {
        super(props)
    }
    render () {
        return (
            <div className="container-fluid">
                {/*<SideNavbar/>*/}
                <TopNavbar/>
            </div>
        )
    }
}

export default App;
