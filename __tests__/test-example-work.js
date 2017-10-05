import React from 'react';
import { shallow } from 'enzyme';
import ExampleWork from '../js/example-work';

const myWork = [
    {
        'title': "Work Example",
        'image': {
            'desc': "example screenshot of a project involving code",
            'src': "images/example1.png",
            'comment': ""
        }
    },
    {
        'title': "Portfolio Boilerplate",
        'image': {
            'desc': "A Serverless Portfolio",
            'src': "/images/example2.png",
            'comment': ""
        }
    }
]

describe("ExampleWork component", () => {
    let component = shallow(<ExampleWork work={myWork}/>);

    it("Should be a 'section element", () => {
        console.log(component.debug());
    })
})