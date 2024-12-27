import React, { useEffect } from 'react';
import { renderAbc } from 'abcjs'; // Ensure abcjs is installed

const AbcNotationRenderer = ({ abcNotation, height }) => {
    useEffect(() => {
        if (abcNotation) {
            renderAbc('abc-output', abcNotation, { responsive: 'resize' });
        }
    }, [abcNotation]);

    return (
        <div style={{ height: `${height}px` }}>
            <div id="abc-output"></div>
        </div>
    );
};

export default AbcNotationRenderer;